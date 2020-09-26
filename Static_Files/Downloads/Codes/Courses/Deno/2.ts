import { serve } from "https://deno.land/std@0.50.0/http/server.ts";

const s = serve({ port: 8000 });

console.log("http://localhost:8000/");

for await (const req of s) {
  if (req.url === "/") {
    req.respond({ body: " h1 This is Index Page /h1" });
  } else {
    req.respond({ body: " h1 Unknown URL /h1" });
  }
}
