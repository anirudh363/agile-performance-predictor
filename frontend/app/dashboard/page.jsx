"use client";

import styles from "./page.module.css";
import { useEffect, useState } from "react";
import Logo from "../../public/assets/logo-nobg.png";
import Image from "next/image";

export default function Dashboard() {
  const steps = ["Team Details", "Sprint Planning", "Sprint Metrics"];

  const [currentStep, setCurrentStep] = useState(1);

  const handleNext = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1);
    }
  };

  return (
    <div className={styles.dashboard}>
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

      <div className={styles.wrapper}>
        <div className={styles.progressVertical}>
          {/* Background vertical line */}
          <div className={styles.verticalLine}></div>

          {steps.map((title, index) => (
            <div key={index} className={styles.stepBlock}>
              <div className={styles.stepContent}>
                <div
                  className={`${styles.circle} ${
                    index + 1 < currentStep
                      ? styles.done
                      : index + 1 === currentStep
                      ? styles.active
                      : ""
                  }`}
                >
                  <span className={styles.label}>
                    {index + 1 < currentStep ? "✓" : index + 1}
                  </span>
                </div>
                <span
                  className={`${styles.title} ${
                    index + 1 <= currentStep ? styles.activeTitle : ""
                  }`}
                >
                  {title}
                </span>
              </div>

              {/* connecting line below step */}
              {index < steps.length - 1 && (
                <div
                  className={`${styles.verticalLineSegment} ${
                    index + 1 < currentStep ? styles.done : ""
                  }`}
                ></div>
              )}
            </div>
          ))}
        </div>
      </div>
      <button
        onClick={handleNext}
        disabled={currentStep === steps.length}
        className={styles.submitButton}
      >
        Submit
      </button>
    </div>
  );
}
