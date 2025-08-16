time="2025-08-16T20:37:21+03:30" level=warning msg="C:\\Users\\Parisa\\shipment-tracking-app\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Building 419.6s (20/24)
 => [internal] load local bake definitions                                                               0.0s
 => => reading from stdin 756B                                                                           0.0s
 => [backend internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 349B                                                                     0.0s
 => [frontend internal] load build definition from Dockerfile                                            0.0s
 => => transferring dockerfile: 520B                                                                     0.0s
 => WARN: FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 1)                           0.0s
 => [frontend internal] load metadata for docker.io/library/node:18-alpine                               2.1s
 => [frontend internal] load metadata for docker.io/library/nginx:alpine                                 2.1s
 => [auth] library/nginx:pull token for registry-1.docker.io                                             0.0s
 => [auth] library/node:pull token for registry-1.docker.io                                              0.0s
 => [backend internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                          0.0s
 => [backend 1/6] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118  197.6s
 => => resolve docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a3  0.0s
 => => sha256:25ff2da83641908f65c3a74d80409d6b1b62ccfaab220b9ea70b80df5a2e0549 446B / 446B               1.0s
 => => sha256:1e5a4c89cee5c0826c540ab06d4b6b491c96eda01837f430bd47f0d26702d6e3 1.26MB / 1.26MB           8.3s
 => => sha256:dd71dde834b5c203d162902e6b8994cb2309ae049a0eabc4efea161b2b5a3d0e 40.01MB / 40.01MB       196.5s
 => => sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870 3.64MB / 3.64MB         108.0s
 => => extracting sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870                0.1s
 => => extracting sha256:dd71dde834b5c203d162902e6b8994cb2309ae049a0eabc4efea161b2b5a3d0e                1.0s
 => => extracting sha256:1e5a4c89cee5c0826c540ab06d4b6b491c96eda01837f430bd47f0d26702d6e3                0.0s
 => => extracting sha256:25ff2da83641908f65c3a74d80409d6b1b62ccfaab220b9ea70b80df5a2e0549                0.0s
 => [backend internal] load build context                                                                1.3s
 => => transferring context: 23.38MB                                                                     1.2s
 => [frontend internal] load .dockerignore                                                               0.0s
 => => transferring context: 2B                                                                          0.0s
 => [frontend stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:2459838ed006e699c252db374550c91  103.7s
 => => resolve docker.io/library/nginx:alpine@sha256:2459838ed006e699c252db374550c91490068bbf3b35fa8b9d  0.0s
 => => sha256:cb1ff4086f82493a4b8b02ec71bfed092cad25bd5bf302aec78d4979895350cb 16.84MB / 16.84MB       102.3s
 => => sha256:a992fbc61ecc9d8291c27f9add7b8a07d374c06a435d4734519b634762cf1c51 1.40kB / 1.40kB           1.8s
 => => sha256:c9ebe2ff2d2cd981811cefb6df49a116da6074c770c07ee86a6ae2ebe7eee926 1.21kB / 1.21kB           1.5s
 => => sha256:7a8a46741e18ed98437271669138116163f14596f411c1948fd7836e39f1afea 405B / 405B               1.5s
 => => sha256:9adfbae99cb79774fdc14ca03a0a0154b8c199a69f69316bcfce64b07f80719f 955B / 955B               2.5s
 => => sha256:403e3f251637881bbdc5fb06df8da55c149c00ccb0addbcb7839fa4ad60dfd04 628B / 628B               3.6s
 => => sha256:6bc572a340ecbc60aca0c624f76b32de0b073d5efa4fa1e0b6d9da6405976946 1.81MB / 1.81MB          49.6s
 => => extracting sha256:6bc572a340ecbc60aca0c624f76b32de0b073d5efa4fa1e0b6d9da6405976946                0.2s
 => => extracting sha256:403e3f251637881bbdc5fb06df8da55c149c00ccb0addbcb7839fa4ad60dfd04                0.0s
 => => extracting sha256:9adfbae99cb79774fdc14ca03a0a0154b8c199a69f69316bcfce64b07f80719f                0.0s
 => => extracting sha256:7a8a46741e18ed98437271669138116163f14596f411c1948fd7836e39f1afea                0.0s
 => => extracting sha256:c9ebe2ff2d2cd981811cefb6df49a116da6074c770c07ee86a6ae2ebe7eee926                0.0s
 => => extracting sha256:a992fbc61ecc9d8291c27f9add7b8a07d374c06a435d4734519b634762cf1c51                0.0s
 => => extracting sha256:cb1ff4086f82493a4b8b02ec71bfed092cad25bd5bf302aec78d4979895350cb                0.3s
 => [frontend internal] load build context                                                               0.0s
 => => transferring context: 7.76kB                                                                      0.0s
 => [frontend 2/6] WORKDIR /app                                                                          0.1s
 => [backend 3/6] COPY package*.json ./                                                                  0.1s
 => [frontend build 3/6] COPY package*.json ./                                                           0.1s
 => ERROR [backend 4/6] RUN npm ci --only=production                                                   218.6s
 => [frontend build 4/6] RUN npm ci                                                                    205.0s
 => [frontend build 5/6] COPY . .                                                                        1.6s
 => CANCELED [frontend build 6/6] RUN npm run build                                                     12.2s
------
 > [backend 4/6] RUN npm ci --only=production:
0.568 npm warn config only Use `--omit=dev` to omit dev dependencies from the install.
20.80 npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
26.36 npm warn deprecated multer@1.4.5-lts.2: Multer 1.x is impacted by a number of vulnerabilities, which have been patched in 2.x. You should upgrade to the latest 2.x version.
217.8 npm error code 1
217.8 npm error path /app/node_modules/puppeteer
217.8 npm error command failed
217.8 npm error command sh -c node install.mjs
217.8 npm error **INFO** Skipping Firefox download as instructed.
217.8 npm error Error: ERROR: Failed to set up chrome v138.0.7204.168! Set "PUPPETEER_SKIP_DOWNLOAD" env variable to skip download.
217.8 npm error     at downloadBrowser (file:///app/node_modules/puppeteer/lib/esm/puppeteer/node/install.js:26:15)
217.8 npm error     at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
217.8 npm error     at async Promise.all (index 0)
217.8 npm error     at async downloadBrowsers (file:///app/node_modules/puppeteer/lib/esm/puppeteer/node/install.js:84:9) {
217.8 npm error   [cause]: Error: Download failed: server returned code 403. URL: https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.168/linux64/chrome-linux64.zip
217.8 npm error       at file:///app/node_modules/@puppeteer/browsers/lib/esm/httpUtil.js:67:31
217.8 npm error       at ClientRequest.requestCallback (file:///app/node_modules/@puppeteer/browsers/lib/esm/httpUtil.js:45:13)
217.8 npm error       at Object.onceWrapper (node:events:632:26)
217.8 npm error       at ClientRequest.emit (node:events:517:28)
217.8 npm error       at HTTPParser.parserOnIncomingClient (node:_http_client:700:27)
217.8 npm error       at HTTPParser.parserOnHeadersComplete (node:_http_common:119:17)
217.8 npm error       at TLSSocket.socketOnData (node:_http_client:541:22)
217.8 npm error       at TLSSocket.emit (node:events:517:28)
217.8 npm error       at addChunk (node:internal/streams/readable:368:12)
217.8 npm error       at readableAddChunk (node:internal/streams/readable:341:9)
217.8 npm error }
217.8 npm notice
217.8 npm notice New major version of npm available! 10.8.2 -> 11.5.2
217.8 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.5.2
217.8 npm notice To update run: npm install -g npm@11.5.2
217.8 npm notice
217.8 npm error A complete log of this run can be found in: /root/.npm/_logs/2025-08-16T17_10_43_721Z-debug-0.log
------
Dockerfile:9

--------------------

   7 |

   8 |     # Install dependencies

   9 | >>> RUN npm ci --only=production

  10 |

  11 |     # Copy application files

--------------------

target backend: failed to solve: process "/bin/sh -c npm ci --only=production" did not complete successfully: exit code: 1
