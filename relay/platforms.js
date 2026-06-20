const platforms = {
    discord: {
        url: process.env.DISCORD_WEBHOOK_URL,
        headers: { 'Content-Type': 'application/json' },
        formatMessage: (msg) => ({ content: msg })
    }
};

function getPlatformConfig(platform) {
    const cfg = platforms[platform?.toLowerCase()];
    
    if (!cfg) {
        throw new Error(`Platform '${platform}' not supported`);
    }
    if (!cfg.url) {
        throw new Error(`DISCORD_WEBHOOK_URL not found in environment`);
    }
    return cfg;
}

module.exports = { getPlatformConfig };