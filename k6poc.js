import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10, // Number of virtual users
  duration: '5s', // Duration of the test
};

const port = '5001'

const url = `http://127.0.0.1:${port}/get-cat-fact`

export default function () {
  // Test GET request
  let getRes = http.get(url);
  check(getRes, { 'GET status was 200': (r) => r.status == 200 });

  // Test POST request
  let postRes = http.post(url, null, { headers: { "Content-Type": "application/json" } });
  check(postRes, { 'POST status was 200 or 201': (r) => [200, 201].includes(r.status) });

  // Test PUT request
  let putRes = http.put(url, null, { headers: { "Content-Type": "application/json" } });
  check(putRes, { 'PUT status was 200 or 201': (r) => [200, 201].includes(r.status) });

  // Think time
  sleep(1);
}