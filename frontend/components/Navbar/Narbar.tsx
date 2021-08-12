import Link from "next/link";
import styles from "./navbar.module.css";

const Navbar = () => (
  <div className={styles.background}>
      <h1 className={styles.title}>Portfolio Creator</h1>
      <ul className={styles.navlist}>
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/portfolio">Templates</Link>
        </li>
        <li>
          <Link href="/about">About</Link>
        </li>
      </ul>
    <div>
      <a href="" className={styles.signin}>
        Sign in
      </a>
      <button className={styles.signup}>Sign Up</button>
    </div>
  </div>
);

export default Navbar;
