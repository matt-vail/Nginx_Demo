FROM nginx:alpine

# Remove the default NGINX configuration
RUN rm -rf /etc/nginx/conf.d/default.conf

# Copy custom NGINX configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80