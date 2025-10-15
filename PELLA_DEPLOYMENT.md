# Pella Deployment Guide for AuraDent Bot

This guide will help you deploy your AuraDent Telegram bot to Pella cloud hosting platform.

## Prerequisites

1. **Telegram Bot Token**: Get one from [@BotFather](https://t.me/botfather)
2. **Admin Chat ID**: Get yours from [@userinfobot](https://t.me/userinfobot)
3. **Pella Account**: Sign up at [pella.dev](https://pella.dev)
4. **GitHub Repository**: Your code should be pushed to GitHub (already done!)

## Deployment Steps

### 1. Prepare Your Bot Token

1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the prompts to create your bot
4. Copy the bot token (format: `123456789:ABCDEF...`)
5. Get your Chat ID from [@userinfobot](https://t.me/userinfobot)

### 2. Deploy to Pella

#### Option A: Deploy Button (Recommended)
1. Click this deploy button: [![Deploy to Pella](https://img.shields.io/badge/Deploy%20to-Pella-blue)](https://pella.dev/deploy?repository=https://github.com/qwerty1199/auradent_bot)
2. Connect your GitHub account if not already connected
3. Configure environment variables (see step 3 below)

#### Option B: Manual Deployment
1. Log in to [Pella Dashboard](https://pella.dev/dashboard)
2. Click "Create New App"
3. Connect your GitHub repository: `qwerty1199/auradent_bot`
4. Choose the deployment branch: `main`

### 3. Configure Environment Variables

In the Pella dashboard, set these environment variables:

| Variable | Value | Example |
|----------|--------|---------|
| `BOT_TOKEN` | Your bot token from BotFather | `123456789:ABCDEF1234567890` |
| `ADMIN_CHAT_ID` | Your Telegram chat ID | `123456789` |
| `WEBHOOK_URL` | Your Pella app URL | `https://your-app-name.pella.app` |
| `EXCEL_FILE_PATH` | Excel file path | `consultations.xlsx` |
| `LOG_LEVEL` | Logging level | `INFO` |

**Important**: The `WEBHOOK_URL` should be your Pella app URL. If your app is named `auradent-bot`, the URL would be `https://auradent-bot.pella.app`

### 4. Deploy and Test

1. Click "Deploy" in the Pella dashboard
2. Wait for the build to complete (usually 2-3 minutes)
3. Check the logs for any errors
4. Test your bot by sending `/start` to your Telegram bot

## Post-Deployment Configuration

### Set Webhook
After deployment, your bot should automatically set up the webhook. You can verify this by checking the Pella logs.

### Test Consultation Flow
1. Send a consultation request to your bot:
   ```
   Name: Test User
   Phone: +1234567890
   Email: test@example.com
   Age: 30
   Consultation Type: General Checkup
   Message: This is a test consultation
   ```
2. Use `/get_consultations` command to download the Excel file
3. Verify the Excel file contains the test data

## File Persistence

**Important**: Pella uses ephemeral file systems, meaning files are not permanently stored. For production use, consider:

1. **Cloud Storage Integration**: Store Excel files in Google Drive, AWS S3, or similar
2. **Database Storage**: Use PostgreSQL or MongoDB add-ons
3. **External File Storage**: Send files to admin immediately after creation

## Monitoring and Logs

- View real-time logs in the Pella dashboard
- Set up log alerts for errors
- Monitor bot performance and response times

## Scaling

- Pella automatically handles scaling based on traffic
- The bot is designed to handle multiple concurrent requests
- Excel files are thread-safe with proper locking

## Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check `BOT_TOKEN` is correct
   - Verify webhook URL is set properly
   - Check Pella logs for errors

2. **Admin commands not working**
   - Verify `ADMIN_CHAT_ID` matches your Telegram chat ID
   - Test with [@userinfobot](https://t.me/userinfobot) to confirm your chat ID

3. **Excel file issues**
   - Check file permissions in logs
   - Verify sufficient memory/storage
   - Consider implementing cloud storage for production

4. **Webhook errors**
   - Ensure `WEBHOOK_URL` matches your Pella app URL exactly
   - Check SSL certificate is valid
   - Verify port configuration

### Getting Help

- Check Pella documentation
- Review bot logs in Pella dashboard  
- Test locally first with polling mode
- Check GitHub issues for known problems

## Security Notes

- Never commit your `.env` file to Git
- Use Pella's environment variable system for secrets
- Regularly rotate your bot token
- Monitor access logs for suspicious activity
- Keep dependencies updated

## Local Development

To test locally before deploying:

1. Copy `.env.example` to `.env`
2. Set your environment variables (leave `WEBHOOK_URL` empty)
3. Run: `python bot.py`
4. The bot will use polling mode for local testing

## Updates and Maintenance

- Push changes to your GitHub repository
- Pella will automatically redeploy from the `main` branch
- Test changes locally first
- Monitor logs after deployments

---

Your AuraDent bot should now be running on Pella! 🎉

For support, check the Pella documentation or create an issue in your GitHub repository.