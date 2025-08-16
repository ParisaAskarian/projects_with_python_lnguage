time="2025-08-16T19:57:58+03:30" level=warning msg="C:\\Users\\Parisa\\shipment-tracking-app\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 9/9
 ✔ redis Pulled                                                                                                   49.8s
   ✔ a976ed7e7808 Pull complete                                                                                    3.7s
   ✔ 0368fd46e3c6 Pull complete                                                                                   21.0s
   ✔ e6fe6f07e192 Pull complete                                                                                   42.8s
   ✔ 4c55286bbede Pull complete                                                                                    2.1s
   ✔ 311eca34042e Pull complete                                                                                   11.4s
   ✔ 5e28347af205 Pull complete                                                                                   21.2s
   ✔ 4f4fb700ef54 Pull complete                                                                                    3.1s
   ✔ a2cadbfeca72 Pull complete                                                                                   42.9s
[+] Building 5.7s (19/24)
 => [internal] load local bake definitions                                                                         0.0s
 => => reading from stdin 756B                                                                                     0.0s
 => [backend internal] load build definition from Dockerfile                                                       0.1s
 => => transferring dockerfile: 349B                                                                               0.0s
 => [frontend internal] load build definition from Dockerfile                                                      0.1s
 => => transferring dockerfile: 520B                                                                               0.0s
 => WARN: FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 1)                                     0.1s
 => [backend internal] load metadata for docker.io/library/node:18-alpine                                          4.3s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                           4.3s
 => [auth] library/nginx:pull token for registry-1.docker.io                                                       0.0s
 => [auth] library/node:pull token for registry-1.docker.io                                                        0.0s
 => [frontend internal] load .dockerignore                                                                         0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [backend internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [backend 1/6] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35c  0.7s
 => => resolve docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc4b8c  0.1s
 => => sha256:25ff2da83641908f65c3a74d80409d6b1b62ccfaab220b9ea70b80df5a2e0549 0B / 446B                           0.4s
 => => sha256:1e5a4c89cee5c0826c540ab06d4b6b491c96eda01837f430bd47f0d26702d6e3 0B / 1.26MB                         0.3s
 => => sha256:dd71dde834b5c203d162902e6b8994cb2309ae049a0eabc4efea161b2b5a3d0e 0B / 40.01MB                        0.3s
 => => sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870 0B / 3.64MB                         0.3s
 => CANCELED [backend internal] load build context                                                                 0.8s
 => => transferring context: 1.23MB                                                                                0.7s
 => [frontend stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:2459838ed006e699c252db374550c91490068bbf3b3  0.8s
 => => resolve docker.io/library/nginx:alpine@sha256:2459838ed006e699c252db374550c91490068bbf3b35fa8b9d29bfe0e31b  0.1s
 => [frontend internal] load build context                                                                         0.8s
 => => transferring context: 2.42MB                                                                                0.7s
 => CANCELED [backend 2/6] WORKDIR /app                                                                            0.0s
 => CACHED [frontend build 3/6] COPY package*.json ./                                                              0.0s
 => CACHED [frontend build 4/6] RUN npm ci                                                                         0.0s
 => CACHED [frontend build 5/6] COPY . .                                                                           0.0s
 => CACHED [frontend build 6/6] RUN npm run build                                                                  0.0s
 => CANCELED [frontend stage-1 2/3] COPY --from=build /app/build /usr/share/nginx/html                             0.0s
 => ERROR [frontend stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf                                    0.0s
------
 > [frontend stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf:
------
Dockerfile:24

--------------------

  22 |

  23 |     # Copy nginx configuration

  24 | >>> COPY nginx.conf /etc/nginx/conf.d/default.conf

  25 |

  26 |     # Expose port

--------------------

target frontend: failed to solve: failed to compute cache key: failed to calculate checksum of ref 1f6rcc6e4o6bfls5lb3oc1mej::1ao0y6w6r72ir5jyrmap6ba3b: "/nginx.conf": not found
