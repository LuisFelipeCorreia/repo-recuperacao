FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM node:20-alpine
WORKDIR /app
COPY --from=builder --chown=node:node /app /app
USER node
EXPOSE 3000
CMD ["node", "server.js"]
