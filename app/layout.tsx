import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"CampRelay — Camp signup readiness",description:"A fictional prototype for planning and monitoring kids' camp registrations."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
