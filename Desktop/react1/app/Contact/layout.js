

export const metadata = {
  title: 'Contact Page',
  description: 'Generated by create next app',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body suppressHydrationWarning>Welcome To {children}</body>
    </html>
  )
}
