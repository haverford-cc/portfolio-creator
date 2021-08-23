##### Build Image #####
FROM node:latest AS builder

WORKDIR /frontend

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

##### Runtime Image #####
FROM node:latest

ENV NEXT_TELEMETRY_DISABLED 1
ENV NODE_ENV production

WORKDIR /usr/src/app

COPY --from=builder /frontend/public ./public
COPY --from=builder /frontend/next.config.js ./next.config.js
COPY --from=builder /frontend/.next/ ./.next
COPY --from=builder /frontend/node_modules/ ./node_modules
COPY --from=builder /frontend/package.json/ ./package.json

CMD ["yarn", "start"]
