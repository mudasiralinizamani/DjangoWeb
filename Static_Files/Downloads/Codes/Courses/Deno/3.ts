import * as datetime from "https://deno.land/std/datetime/mod.ts";

console.log(datetime.currentDayOfYear());

// Oak is Sarting

import * as oak from "https://deno.land/x/oak/mod.ts";

const App = new oak.Application();

const port = 3000;

App.use((ctx) => {
  ctx.response.body = "Hello World";
});

App.listen({ port });

console.log("Server is Running on 'localhost:3000'");
