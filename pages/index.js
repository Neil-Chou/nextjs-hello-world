import Link from 'next/link'
const Index = () => (
  <div>
    <br></br>
    Name of folder is the UTC time when it generates.&nbsp;&nbsp;&nbsp;{' '}<Link href="/about"><a>About</a></Link> <br></br><br></br><br></br>
    <br></br>
      <Link href="/2022-12-22_00:31:07">
        <a>"/2022-12-22_00:31:07"</a>
      </Link>
    <br></br>
  </div>
)
export default Index;
