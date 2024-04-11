FROM nginx:latest

RUN apt-get update && apt-get install -y curl

COPY nginx.conf /etc/nginx/nginx.conf

RUN addgroup --system nginxuser && adduser --system --no-create-home --ingroup nginxuser nginxuser && \
    mkdir -p /var/cache/nginx/client_temp /var/cache/nginx/proxy_temp /tmp/nginx/ /tmp/nginx/conf.d && \
    chown -R nginxuser:nginxuser /var/cache/nginx /tmp/nginx/ && \
    chmod -R 755 /tmp/nginx/

RUN rm /etc/nginx/conf.d/default.conf

ENV NGINX_ENVSUBST_OUTPUT_DIR=/tmp/nginx/conf.d
USER nginxuser

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
 CMD curl --fail http://localhost:8080/admin/ || exit 1
