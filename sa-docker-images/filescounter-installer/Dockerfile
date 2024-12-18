FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the system and install dependencies for installing .deb packages
RUN apt-get update && apt-get install -y \
    dpkg \
    && apt-get clean

# Copy the .deb package into the container
# Replace `your-package.deb` with the name of your .deb file
COPY filescounter_1.0_all.deb /tmp/filescounter_1.0_all.deb

# Install the .deb package
RUN dpkg -i /tmp/filescounter_1.0_all.deb || apt-get install -f -y

# Execute the installed script with the provided arguments
# Replace `your-installed-script` with the actual script name installed by your .deb package
CMD ["bash", "-c", "filescounter.bash -p \"$HOME\""]
