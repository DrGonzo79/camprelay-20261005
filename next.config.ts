import type {NextConfig} from "next";
const repo=process.env.GITHUB_REPOSITORY?.split("/")[1];
const pages=process.env.GITHUB_ACTIONS==="true"&&process.env.NODE_ENV==="production"&&Boolean(repo);
const config:NextConfig={output:"export",trailingSlash:true,images:{unoptimized:true},basePath:pages?`/${repo}`:"",assetPrefix:pages?`/${repo}/`:""};
export default config;
