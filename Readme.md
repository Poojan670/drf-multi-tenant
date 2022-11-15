<p align="center">
  <a href="https://i0.wp.com/www.spritle.com/blogs/wp-content/uploads/2019/11/Dj-690520.png?resize=691%2C521&ssl=1"><img src="https://i0.wp.com/www.spritle.com/blogs/wp-content/uploads/2019/11/Dj-690520.png?resize=691%2C521&ssl=1" alt="Spring Boot" height="100%" width="100%"></a>
</p>

<p align="center">
    <em>Multi Tenancy Sample Study in Django Rest Framework</em>
</p>

---

**Source Code**:

https://github.com/Poojan670/drf-multi-tenant

Software multitenancy is a software architecture in which a single instance of software runs on a server and serves multiple tenants. Systems designed in such manner are "shared". A tenant is a group of users who share a common access with specific privileges to the software instance.


Potential benefits of multi-tenant:

Affordable Cost: Multiple customers means that the cost for the environment is shared, and those savings (from the SaaS vendor) are typically transferred to the cost of the software.
Integrations: Cloud environments allow for easier integration with other applications through the use of APIs.
“Hands-free” Maintenance: The server technically belongs to the SaaS vendor, meaning that a certain level of database maintenance is handled by the vendor, instead of you maintaining the environment yourself.
Potential drawbacks of multi-tenant:

Limited Management/Customization: While you do have added integration benefits, custom changes to the database aren’t typically an option.
Security: Other tenants won’t see your data. However, multiple users (not associated with your organization) are allowed on the same database. This broader access reduces control of security.
Updates/Changes: If you’re reliant on integrations with other SaaS products and one updates their system, it may cause issues with those connecting apps.
---


<div class="termy">


***SETUP***

Setup an .env file in the respective folder structure with following sample
```console
 // For DRF & Postgres Configurations

SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=
DB_DEFAULT=
DB_TEST=
DB_DEVELOPMENT=
```
</div>


<div class="termy">

Create a virtual environment

_python -m venv env_

Activate the virtual environment

_env/Scripts/activate_

Install Using pip package

```console
$ pip install -r requirements.txt
```
</div>


<div class="termy">

Perform the DB migrations in django

```console
$ py manage.py migrate

For multi db
$ py manage.py migrate --database=DB_NAME

$ py tenant_manage.py createsuperuser

For multi db:
$ py tenant_manage.py DB_NAME createsuperuser --database=DB_NAME
```
</div>


<div class="termy">

For MultiDB-Setup
```console
On Windows:

Edit the windows/system32/etc/hosts/ by adding your db.host.local 

and run 
$py manage.py runserver
```
</div>