FROM nginx:1.11.3
ARG APP_ENV=dev
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY app.${APP_ENV}.conf /etc/nginx/conf.d/
