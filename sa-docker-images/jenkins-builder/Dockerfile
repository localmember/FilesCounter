FROM jenkins/jenkins:lts-jdk17

# Switch to root for package installation
USER root

# Install necessary tools (optional, adjust based on your build requirements)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    unzip \
    && apt-get clean

# Switch back to the Jenkins user
USER jenkins

# Set the Jenkins home directory
ENV JENKINS_HOME=/var/jenkins_home

# Pre-install Jenkins plugins from a plugins.txt file
COPY required_builder/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugins < /usr/share/jenkins/ref/plugins.txt

# Copy the initialization script
COPY required_builder/initial-setup.groovy /usr/share/jenkins/ref/init.groovy.d/initial-setup.groovy

# Expose the default Jenkins ports
EXPOSE 8080 50000

# Set the default startup command
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
