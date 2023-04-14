"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const api_1 = require("@atproto/api");
const bsky = new api_1.BskyAgent({ service: 'https://bsky.social' });
// sign in using my username and password
const res = await bsky.com.atproto.session.create({}, {
    username: 'shreyan.bsky.social',
    password: '!'
});
// configure future calls to include the token in the Authorization header
bsky.setHeader('Authorization', `Bearer ${res.data.accessJwt}`);
const posts = await bsky.com.atproto.repo.listRecords({
    repo: 'pfrazee.com',
    type: 'app.bsky.post'
});
console.log(posts);
//# sourceMappingURL=atproto.js.map