const fetch = require('node-fetch');
const { getPlatformConfig } = require('./platforms');

module.exports = async function (context, req) {
    context.log('Relay triggered');

    const { platform, message } = req.body || {};

    if (!platform ||!message) {
        context.res = { 
            status: 400, 
            body: { error: "Need 'platform' and 'message' in JSON body" } 
        };
        return;
    }

    try {
        const cfg = await getPlatformConfig(platform);
        let result;

        if (cfg.post) {
            // For OAuth platforms like YouTube, Facebook, LinkedIn
            context.log(`Using OAuth post for ${platform}`);
            result = await cfg.post(message);
            result.platform = platform;
        } else {
            // For webhook platforms like Discord, Slack, Telegram
            context.log(`Using webhook for ${platform}`);
            const response = await fetch(cfg.url, {
                method: 'POST',
                headers: cfg.headers,
                body: JSON.stringify(cfg.formatMessage(message))
            });
            
            result = {
                platform: platform,
                status: response.ok? 'success' : 'error',
                code: response.status
            };
            
            if (!response.ok) {
                const errText = await response.text();
                result.error = errText;
            }
        }

        context.res = { 
            status: 200, 
            body: { message: 'Blast complete', results: [result] } 
        };

    } catch (err) {
        context.log.error(`Error: ${err.message}`);
        context.res = {
            status: 500,
            body: { 
                message: 'Blast complete', 
                results: [{ platform, status: 'error', error: err.message }] 
            }
        };
    }
};