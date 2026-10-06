// Bounded metadata leads for the 2026-04-05 BJT supplement, not public-date proof.
import { writeFile } from 'node:fs/promises';
const out = new URL('./', import.meta.url);
const slice = 'submittedDate:[202604041600 TO 202604051559]';
const routes = [
  ['model', '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")'],
  ['system', '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:LLM OR all:GPU OR all:inference OR all:"model training")'],
  ['multi', '(cat:cs.CV OR cat:cs.RO) AND (all:multimodal OR all:"world model" OR all:"vision language action" OR all:"generative model" OR all:diffusion)'],
  ['agent', '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM OR all:"foundation model" OR all:"retrieval augmented" OR all:"tool calling")'],
];
for (const [id, topic] of routes) {
  const query = `(${slice}) AND (${topic})`;
  const url = 'https://export.arxiv.org/api/query?' + new URLSearchParams({search_query:query,start:'0',max_results:'100',sortBy:'lastUpdatedDate',sortOrder:'ascending'});
  const at = new Date().toISOString();
  let receipt;
  try {
    const response = await fetch(url,{signal:AbortSignal.timeout(20000)});
    const body = await response.text();
    await writeFile(new URL(`SUP_arxiv-${id}-submitted_20261013.raw`,out),body);
    receipt = {url,at,query,start:0,maxResults:100,status:response.status,bytes:Buffer.byteLength(body)};
  } catch (error) { receipt = {url,at,query,error:String(error)}; }
  await writeFile(new URL(`SUP_arxiv-${id}-submitted_20261013.request.json`,out),JSON.stringify(receipt,null,2)+'\n');
  console.log(JSON.stringify(receipt));
}
