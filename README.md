# Tissue Salt Wellness Assessment

A comprehensive web application for tissue salt consultations by Dr. Aliki V. Strydom-Hensen.

## Features

✅ **User Authentication**
- Demo login system with database integration
- Session management
- Guest mode for quick access

✅ **Payment Processing**
- Stripe test mode integration
- Multiple service tiers ($5 - $220)
- Secure payment forms

✅ **Age-Based Assessments**
- Infant questionnaires (0-3 years)
- Basic assessment (15 questions)
- Advanced assessment (30 questions)

✅ **Facial Analysis**
- Photo upload functionality
- Simulated AI analysis
- Schüssler facial diagnosis method
- Tissue salt recommendations based on facial features

✅ **Assessment History**
- User dashboard
- Past assessment tracking
- Results persistence
- Mobile-friendly interface

✅ **Tissue Salt Database**
- 12 primary tissue salts
- Detailed descriptions and benefits
- Symptom-to-salt mappings
- Evidence-based recommendations

## Demo Credentials

**Login**: Any email/password combination works for testing
- Example: test@example.com / password123

**Payment**: Use Stripe test cards
- Card: 4242 4242 4242 4242
- Expiry: Any future date (e.g., 12/25)
- CVC: Any 3 digits (e.g., 123)
- ZIP: Any 5 digits (e.g., 12345)

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser to: `http://localhost:8080`

## Project Structure

```
tissue-salts-production/
├── app.py                 # Flask backend server
├── index.html            # Frontend single-page application
├── tissue_salts.db       # SQLite database
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version specification
├── DEPLOYMENT.md        # Comprehensive deployment guide
└── README.md            # This file
```

## Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask
- **Database**: SQLite (development) / PostgreSQL (production)
- **Payment**: Stripe API (test mode)
- **Deployment**: Heroku, Railway, DigitalOcean, Render compatible

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment instructions including:
- Railway (recommended)
- Heroku
- DigitalOcean
- Render
- PythonAnywhere

## Current Status

🎯 **Demo Version** - Fully functional with simulated features

This is a demonstration version designed to showcase the application's capabilities. All core features are working:
- ✅ Login and authentication
- ✅ Payment processing
- ✅ Questionnaire system
- ✅ Facial analysis
- ✅ Results calculation
- ✅ History tracking

## Future Enhancements

- Real authentication system
- Live payment processing
- AI-powered facial analysis
- Email notifications
- Custom blend ordering
- Video consultation booking
- Hair mineral analysis integration
- Admin dashboard
- Analytics and reporting

## Database Schema

### Users Table
- id (PRIMARY KEY)
- email (UNIQUE)
- password_hash
- created_at

### Sessions Table
- id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- token (UNIQUE)
- created_at

### Assessments Table
- id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- service_type
- age_group
- answers (JSON)
- results (JSON)
- order_number
- created_at

## API Endpoints

- `POST /api/register` - User registration
- `POST /api/login` - User login
- `POST /api/verify-session` - Session verification
- `POST /api/logout` - User logout
- `POST /api/save-assessment` - Save assessment results
- `POST /api/get-assessments` - Retrieve user's assessment history

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Mobile Responsive

✅ Fully tested on iPhone and Android devices
✅ Touch-friendly interface
✅ Optimized layouts for small screens

## License

Proprietary - Dr. Aliki V. Strydom-Hensen

## Contact

For questions or support, please contact Dr. Aliki.

---

**Version**: 1.0.0 (Demo)
**Last Updated**: October 2025

