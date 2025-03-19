import styles from './page.module.css';
import Image from "next/image";
import box1_img from "../../../public/assets/box1.png";
import Link from 'next/link';

export default function HomePage() {
  return (
    <section id="home">
      <main className={styles.main}>
        <div className={styles.box1}>
          <div className={styles.box1_content}>
            <h2>Experience Data-Driven Agile Planning</h2>
            <p>Enhance Your Agile Workflow with AI-Powered Predictions</p>
            <button className={styles.button}>
              <div className={styles.button_overlay}></div>
              <span>
                Know More
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="40"
                  viewBox="0 -960 960 960"
                  width="30"
                >
                  <path d="M320-200v-560l440 280-440 280Zm80-280Zm0 134 210-134-210-134v268Z" />
                </svg>
              </span>
            </button>
          </div>
          <Image
            src={box1_img}
            alt="Dog"
            width={70}
            quality={100}
            placeholder="blur"
            className={styles.box1_img}
          />
        </div>

        <div className={styles.boxContainer}>
          <div className={styles.box2}>
            <div className={styles.box2Content}>
              <div className={styles.textContent}>
                <h3>Experience Agile Predictions Instantly!</h3>
                <p>Curious about how our model works?</p>
                <p>Try it instantly - no signup required!</p>
              </div>
              <button className={styles.tryNowButton}>Try Now</button>
            </div>
          </div>

          <div className={styles.box3}>
            <div className={styles.box3Content}>
              <div className={styles.textContent}>
                <h3>
                  Unlock Full Insights with a <br /> Personlized Dashboard
                </h3>
                <p>
                  Save your predictions, compare your result and <br />
                  gain deeper insights into your team's efficiency
                </p>
              </div>
              <Link href="/signup">
                <button className={styles.tryNowButton}>Sign Up</button>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </section>
  );
}
