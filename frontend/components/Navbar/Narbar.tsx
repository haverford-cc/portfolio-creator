import Link from "next/link";
import styles from "./navbar.module.css";

const Navbar = () => (
  <div className={styles.background}>
    <div className={styles.logo}>
      <h1 className={styles.title}>Portfolio Creator</h1>
    </div>
    <div className={styles.middle}>
      <ul className={styles.navlist}>
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/about">About</Link>
        </li>
        <li>
          <Link href="/portfolio">Templates</Link>
        </li>
      </ul>
    </div>
    <div className={styles.right}>
      <a href="" className={styles.signin}>
        Sign in
      </a>
      <button className={styles.signup}>Sign Up</button>
    </div>
  </div>
);

export default Navbar;
