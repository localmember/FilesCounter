import jenkins.model.*
import hudson.security.*

def instance = Jenkins.getInstance()
def hudsonRealm = new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount("admin", "admin") // Set default credentials
instance.setSecurityRealm(hudsonRealm)
instance.save()
