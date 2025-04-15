import Logo from '../../../public/assets/logo-1.png';
import styles from './page.module.css';
import Image from 'next/image';

export default function DashboardNav() {
  return (
    <div className={styles.navbar}>
      <Image
        src={Logo}
        alt="Dog"
        width={70}
        quality={100}
        placeholder="blur"
        className={styles.agile_logo}
      />
      <p>Agile Performance Predictor</p>
    </div>
  );
}
