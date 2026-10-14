# Swiggy coupon service — measure the image before you cut it

`GET /coupon` returns a coupon. The `Dockerfile` here works and produces an image you would
be embarrassed to deploy.

## The exact command that prints an image's size

So that everybody's number means the same thing:

    docker image ls --format '{{.Repository}}:{{.Tag}}  {{.Size}}' coupons

Build it first, and write the number down before you change anything:

    docker build -t coupons:before .

## Run it

    docker run --rm -p 8080:8080 coupons:before
    curl localhost:8080/coupon
