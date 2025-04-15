// app/dashboard/page.js
"use client";

import styles from "./page.module.css";
import { useEffect, useState } from "react";
import Logo from "../../public/assets/logo-1.png";
import ButtomLeftImage from "../../public/assets/form-1-removebg.png";
import Image from "next/image";

// import the step forms
import TeamDetailsForm from "../components/Team-Form/TeamDetailsForm";
import SprintPlanningForm from "../components/Sprint-Planning/SprintPlanningForm";
import SprintMetricsForm from "../components/Sprint-Metrics/SprintMetricsForm";

export default function Dashboard() {
  const steps = ["Team Details", "Sprint Planning", "Sprint Metrics"];
  const [currentStep, setCurrentStep] = useState(1);
  const [sprintStartDate, setSprintStartDate] = useState();
  const [sprintEndDate, setSprintEndDate] = useState();


  const handleNext = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrevious = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  // choose which component to render based on current step
  const renderForm = () => {
    switch (currentStep) {
      case 1:
        return (
          <TeamDetailsForm
            currentStep={currentStep}
            steps={steps}
            handleNext={handleNext}
            
          />
        );
      case 2:
        return (
          <SprintPlanningForm
            currentStep={currentStep}
            steps={steps}
            handleNext={handleNext}
            handlePrevious={handlePrevious}
            setSprintStartDate={setSprintStartDate}
            setSprintEndDate={setSprintEndDate}
          />
        );
      case 3:
        return (
          <SprintMetricsForm
            currentStep={currentStep}
            steps={steps}
            handlePrevious={handlePrevious}
            sprintStartDate={sprintStartDate}
            sprintEndDate={sprintEndDate}
          />
        );
      default:
        return <div>End of forms</div>;
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

      {/* Render current form */}
      {renderForm()}

      <Image
        src={ButtomLeftImage}
        alt="Decorative"
        className={styles.bottomLeftImage}
        quality={100}
      />

      <div className={styles.rightStrip}></div>
    </div>
  );
}
