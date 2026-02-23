FROM node:20-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY src ./src
COPY next.config.mjs .
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0", "-p", "3000"]
