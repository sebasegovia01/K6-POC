import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10, // Number of virtual users
  duration: '5s', // Duration of the test
};

export default function () {
  // Test GET request
  let getRes = http.get('http://127.0.0.1:5000/get-cat-fact');
  check(getRes, { 'GET status was 200': (r) => r.status == 200 });

  // Test POST request
  let postRes = http.post('http://127.0.0.1:5000/post-cat-fact', null, { headers: { "Content-Type": "application/json" } });
  check(postRes, { 'POST status was 200 or 201': (r) => [200, 201].includes(r.status) });

  // Test PUT request
  let putRes = http.put('http://127.0.0.1:5000/put-cat-fact', null, { headers: { "Content-Type": "application/json" } });
  check(putRes, { 'PUT status was 200 or 201': (r) => [200, 201].includes(r.status) });

  // Think time
  sleep(1);
}