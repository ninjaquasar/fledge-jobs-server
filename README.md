# :briefcase: FledgeJobs

> ***Where Talent Meets Opportunity***

---

## :dart: Project Overview
**FledgeJobs** is a feature-rich job board web application built to connect *Employers* (Recruiters) with *Job Seekers*. The platform provides a seamless experience for posting, finding, and applying for jobs in an efficient and user-friendly system.

---

### Project Link: [`fledgejobs.vercel.app`](https://fledgejobs.vercel.app/)

---

## :gem: Features
#### :mag: For Job Seekers:
- Browse and search job listings
- Apply for jobs by submitting resume
- Track job applications submitted
- Authenticated user dashboard

#### :memo: For Employers:
- Create, update, and delete job listings
- View applications received per job
- Accept or reject applications
- Authenticated employer dashboard

#### :construction_worker: Admin Features:
- Manage users, jobs, and applications
- Monitor platform activities

---

## 🛠️ Technologies Used
- **Front-End:** [React](https://react.dev) *(Coming Soon)*.
- **Back-End:** [Django](https://www.djangoproject.com), [Django REST Framework](https://www.django-rest-framework.org) (DRF), [Djoser](https://djoser.readthedocs.io/) + [JWT Auth](https://djoser.readthedocs.io/en/latest/authentication_backends.html#json-web-token-authentication).
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **API Documentation:** [drf-yasg](https://drf-yasg.readthedocs.io/) (Swagger/Redoc)
- **Deployment:** [Vercel](https://vercel.com/)

---
## 📦 Packages Used
- **Django:**
    - Django ([Official](https://www.djangoproject.com/) | [PyPi](https://pypi.org/project/Django/) | [ReadTheDocs](https://django.readthedocs.io/en/stable/))
- **Django REST Framework:**
    - rest_framework ([Official](https://www.django-rest-framework.org/) | [PyPi](https://pypi.org/project/djangorestframework/))
- **Authentication:**
    - djoser ([PyPi](https://pypi.org/project/djoser/) | [ReadTheDocs](https://djoser.readthedocs.io/en/latest/))
    - rest_framework_simplejwt ([PyPi](https://pypi.org/project/djangorestframework-simplejwt/) | [ReadTheDocs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/))
- **Database:**
    - psycopg2-binary ([Official](https://www.psycopg.org/docs/) | [PyPi](https://pypi.org/project/psycopg2-binary/))
- **Environment Variable:**
    -  python-decouple ([PyPi](https://pypi.org/project/python-decouple/))
- **API Documentation:**
    - drf-yasg ([PyPi](https://pypi.org/project/drf-yasg/) | [ReadTheDocs](https://drf-yasg.readthedocs.io/en/stable/))

---

## 🔗 Project Endpoints

**Endpoints:**
- `/auth/` - Authentication Endpoints
    - `/jwt/` - JWT Authentication Token Endpoints
    - `/users/` - Users Information Endpoints
- `/api/v1/` - API Endpoints
    - `/jobs/` - Jobs management Endpoints
    - `/categories/` - Categories management Endpoints
- `/ref/` - References/Documentations Endpoints (Go to the next section for more information)

---

## 📄 API Documentation
**Interactive API Docs that will guide you with using our APIs**

Swagger Documentation (Best for Developers, Recommended for everyone):
```
https://fledgejobs.vercel.app/ref/api/
```
Redoc Documentation (Another nice choice):
```
https://fledgejobs.vercel.app/ref/api/redoc/
```

---

## 👨‍💻 Credits
**Manager:** Me

**Developer:** Me

**Tester:** Me

Made with 💙 by **Rakibul Islam** ([@riaurko](https://github.com/riaurko))

---

## 🫱🏽‍🫲🏼 Contribution
Feel free to fork this repo, submit issues, or open pull requests. See [CONTRIBUTING.md](./CONTRIBUTING.md) for more information about Contributing.

---

## 📜 License
Licensed under the [BSD License](LICENSE).

