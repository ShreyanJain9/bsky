import { BskyAgent } from '@atproto/api';

const bsky = new BskyAgent({ service: 'https://bsky.social' });

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
