# Base image for Jenkins
FROM jenkins/jenkins:lts-jdk17

# Set environment variables
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Pre-install plugins
COPY required_master/plugins.txt /tmp/plugins.txt

# Install plugins using the copied file
RUN jenkins-plugin-cli --plugins < /tmp/plugins.txt

# Expose required ports
EXPOSE 8080 50000

# Set up default admin user
COPY required_master/initial-setup.groovy required_master/initial-setup.groovy
