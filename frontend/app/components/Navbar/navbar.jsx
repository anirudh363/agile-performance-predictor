import styles from './page.module.css';
import Image from 'next/image';
import Logo from '../../../public/assets/logo.png';
import Link from 'next/link';

export default function Navbar() {
    return (
      <div className={styles.home_page}>
        <nav className={styles.navbar}>
          <div className={styles.title}>
            <Image
              src={Logo}
              alt="Dog"
              width={70}
              quality={100}
              placeholder="blur"
            />
            Agile Performance Predictor
          </div>
          <ul>
            <li>
              <a href="#home">Home</a>
            </li>
            <li>
              <a href="#aboutus">About us</a>
            </li>
            <li>
              <a href="#contact">Contact</a>
            </li>
          </ul>
          <Link href="/login">
            <button className={styles.button}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 -960 960 960"
                // fill="#e3e3e3"
                className={styles.icon}
              >
                <path d="M480-120v-80h280v-560H480v-80h280q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H480Zm-80-160-55-58 102-102H120v-80h327L345-622l55-58 200 200-200 200Z" />
              </svg>
              Login
            </button>
          </Link>
        </nav>
      </div>
    );
}

// <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M480-120v-80h280v-560H480v-80h280q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H480Zm-80-160-55-58 102-102H120v-80h327L345-622l55-58 200 200-200 200Z"/></svg>