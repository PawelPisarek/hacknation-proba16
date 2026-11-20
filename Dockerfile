FROM node:22-alpine
WORKDIR /app
COPY app/ ./
ENV PORT=3000
EXPOSE 3000
CMD ["node", "serwer.mjs"]
