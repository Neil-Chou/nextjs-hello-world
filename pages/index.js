import Link from 'next/link'
const Index = () => (
  <div>
    Name of folder is the UTC time when it generates.{' '}
    <br></br>
      <Link href="/2022-12-21 22:14:46.265782">
        <a>"/2022-12-21 22:14:46.265782"</a>
      </Link>
    <br></br>
      <Link href="/about">
        <a>About</a>
      </Link>
    <br></br>
      <Link href="/day">
        <a>day</a>
      </Link>
  </div>
)
export default Index;
