import styles from "./page.module.css";
import Navbar from "./components/Navbar/navbar";
import HomePage from "./components/Home/home";

export default function Home() {
  return (
    <div className={styles.home_page}>
      <div className={styles.navbar}>
        <Navbar />
      </div>
      <div className={styles.home_page}>
        <HomePage />
      </div>

      <section id="about" className={styles.section}>
        About Us Content
      </section>
      <section id="contact" className={styles.section}>
        Contact Content
      </section>
    </div>
  );
}
