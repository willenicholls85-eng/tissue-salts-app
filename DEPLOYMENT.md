# Tissue Salt Wellness Assessment - Deployment Guide

## Overview

This is a comprehensive tissue salts consultation web application demo for Dr. Aliki V. Strydom-Hensen. The application includes:

- User authentication (demo mode)
- Payment processing (Stripe test mode)
- Age-based health assessments with questionnaires
- Facial analysis for tissue salt recommendations
- User history tracking
- SQLite database backend

## Current Status

✅ **Fully Functional Demo Application**
- All features working and tested
- Mobile-responsive design
- Database integration complete
- Ready for deployment

## Technology Stack

- **Frontend**: Single-page HTML application with vanilla JavaScript and CSS
- **Backend**: Python Flask server
- **Database**: SQLite (development) - can be upgraded to PostgreSQL for production
- **Deployment**: Configured for Heroku, Railway, or any Python hosting platform

## Quick Start (Local Development)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access at: `http://localhost:8080`

## Deployment Options

### Option 1: Railway (Recommended - Free Tier Available)

Railway offers easy deployment with automatic HTTPS and persistent storage.

1. **Create Railway Account**: Visit https://railway.app and sign up

2. **Install Railway CLI** (optional):
```bash
npm install -g @railway/cli
```

3. **Deploy via GitHub**:
   - Push this code to a GitHub repository
   - Connect Railway to your GitHub account
   - Select the repository
   - Railway will auto-detect Flask and deploy

4. **Deploy via CLI**:
```bash
railway login
railway init
railway up
```

5. **Add Environment Variables** (if needed):
   - Go to your Railway project settings
   - Add any required environment variables

6. **Database**: Railway provides PostgreSQL add-on if you need to upgrade from SQLite

**Cost**: Free tier includes 500 hours/month, $5/month for hobby plan

### Option 2: Heroku

1. **Create Heroku Account**: Visit https://heroku.com

2. **Install Heroku CLI**:
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Ubuntu/Debian
curl https://cli-assets.heroku.com/install.sh | sh
```

3. **Login and Create App**:
```bash
heroku login
heroku create tissue-salts-app
```

4. **Deploy**:
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku main
```

5. **Open Your App**:
```bash
heroku open
```

**Cost**: Free tier discontinued, starts at $7/month per dyno

### Option 3: DigitalOcean App Platform

1. **Create DigitalOcean Account**: Visit https://digitalocean.com

2. **Create New App**:
   - Go to App Platform
   - Connect your GitHub repository
   - Select this repository
   - DigitalOcean auto-detects Python/Flask

3. **Configure**:
   - Set build command: `pip install -r requirements.txt`
   - Set run command: `gunicorn app:app`
   - Choose instance size

4. **Deploy**: Click "Create Resources"

**Cost**: Starts at $5/month for basic tier

### Option 4: Render

1. **Create Render Account**: Visit https://render.com

2. **Create New Web Service**:
   - Connect GitHub repository
   - Select this repository
   - Render auto-detects Flask

3. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Deploy**: Click "Create Web Service"

**Cost**: Free tier available with limitations, $7/month for starter

### Option 5: PythonAnywhere

1. **Create Account**: Visit https://pythonanywhere.com

2. **Upload Files**:
   - Use the Files tab to upload all project files
   - Or clone from GitHub

3. **Create Web App**:
   - Go to Web tab
   - Add new web app
   - Choose Flask
   - Point to your app.py

4. **Configure**:
   - Set working directory
   - Install requirements via Bash console

**Cost**: Free tier available, $5/month for basic

## Database Upgrade (Production)

For production deployment, upgrade from SQLite to PostgreSQL:

1. **Update requirements.txt**:
```
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

2. **Update app.py** to use PostgreSQL:
```python
import os
DATABASE = os.environ.get('DATABASE_URL', 'sqlite:///tissue_salts.db')
# Update connection code accordingly
```

3. **Add PostgreSQL** on your hosting platform

## Environment Variables

For production, set these environment variables:

- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key-here` (generate a secure random key)
- `DATABASE_URL=your-database-url` (if using PostgreSQL)

## Post-Deployment Checklist

- [ ] Test login functionality
- [ ] Test payment flow with Stripe test cards
- [ ] Complete a questionnaire assessment
- [ ] Test facial analysis upload
- [ ] Check assessment history/dashboard
- [ ] Verify mobile responsiveness
- [ ] Test on different browsers
- [ ] Set up custom domain (optional)
- [ ] Configure SSL/HTTPS (usually automatic)
- [ ] Set up monitoring/logging

## Custom Domain Setup

Most platforms support custom domains:

1. **Purchase Domain**: From Namecheap, Google Domains, etc.

2. **Add to Platform**:
   - Go to your app settings
   - Add custom domain
   - Follow DNS configuration instructions

3. **Update DNS**:
   - Add CNAME record pointing to your app URL
   - Wait for DNS propagation (up to 48 hours)

## Upgrading to Production

This is currently a **demo version**. To upgrade to production:

### Authentication
- Replace demo login with real authentication
- Integrate OAuth providers (Google, Facebook)
- Add password reset functionality
- Implement email verification

### Payment Processing
- Switch from Stripe test mode to live mode
- Add real API keys
- Implement webhook handlers for payment confirmation
- Add invoice generation

### Facial Analysis
- Integrate real AI/ML model for facial analysis
- Use computer vision APIs (AWS Rekognition, Google Vision)
- Implement Schüssler facial diagnosis algorithm
- Add image preprocessing and validation

### Email Integration
- Add SendGrid or Mailgun for email delivery
- Send assessment results via email
- Add appointment confirmation emails
- Implement email templates

### Additional Features
- Add child (4-17 years) questionnaires
- Add adult (18+) questionnaires
- Implement custom blend ordering system
- Add video consultation booking
- Integrate hair mineral analysis ordering
- Add practitioner admin dashboard
- Implement analytics and reporting

## Support

For questions or issues:
- Email: support@example.com
- Documentation: [Link to docs]

## License

Proprietary - Dr. Aliki V. Strydom-Hensen

---

**Current Version**: 1.0.0 (Demo)
**Last Updated**: October 2025

