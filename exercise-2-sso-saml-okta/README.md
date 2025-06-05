## 🛡 Okta SSO Integration – Support Response

*Hi [Customer Name],*

Thanks for reaching out. Port supports SSO via *SAML 2.0, which works with identity providers like **Okta, **Azure AD, and **Google Workspace*. Since you're using Okta, we can help you set up the connection smoothly.

To get started, create a new *SAML 2.0 app* in your Okta dashboard by navigating and clicking on Applications. Use these values:  
- *Sign-in URL:* https://auth.getport.io/login/callback?connection=your-connection-name  
- *Entity ID (Audience URI):* urn:auth0:port-prod:your-connection-name  
-  we will provide you with your *connection name*

Then map the following attributes:  
- email → user.email  
- given_name → user.firstName  
- family_name → user.lastName  
- email_verified → true

Once that’s done, click Finish to create the application and generate a PEM format certificate, please send us your:
- *PEM certificate*
- *Metadata URL* (or file)

We’ll reply with your unique *connection name*,*sign-in URL*, *Entity ID*, and any additional configuration info needed to finalize the setup.

You can learn more here:  
[Port SAML + Okta Integration Guide](https://docs.port.io/sso-rbac/sso-providers/saml/okta)

Let me know if you'd like support testing the login after integration or setting up group-based access controls.

—
Rofiat Abdulkareem
Support Engineer Candidate
