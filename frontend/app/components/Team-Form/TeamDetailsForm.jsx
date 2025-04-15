// components/TeamDetailsForm.js
"use client";

import styles from './page.module.css'
import { useState } from "react";
import Info from '../Info/Info';

export default function TeamDetailsForm({ currentStep, steps, handleNext }) {
  const [activeForm, setActiveForm] = useState("create");

  return (
    <div className={styles.container}>
      <h2 className={styles.form_title}>Team Details</h2>
      <div className={styles.toggle}>
        <button
          className={activeForm === "create" ? styles.active : ""}
          onClick={() => setActiveForm("create")}
        >
          Creating a new name
        </button>
        <button
          className={activeForm === "choose" ? styles.active : ""}
          onClick={() => setActiveForm("choose")}
        >
          Choose from the existing
        </button>
      </div>

      <Info/>

      <div className={styles.formContent}>
        {activeForm === "create" ? (
          <form className={styles.form_1}>
            <h3>What is your team name?</h3>
            <input type="text" placeholder="Example: Gladwell" />
            <p className={styles.stupidTagLine}>
              Every winning team has a name--pick yours!
            </p>
          </form>
        ) : (
          <form className={styles.form_2}>
            <h3>What is your team name?</h3>
            <div className={styles.selectTeamDiv}>
              <p className={styles.stupidTagLine}>
                Choose from your saved team names--no need to start from
                scratch!
              </p>
              <select>
                <option>Select Team</option>
                <option>Name 1</option>
                <option>Name 2</option>
              </select>
            </div>
          </form>
        )}
      </div>

      <div className={styles.buttonWrapper}>
        <button
          type="submit"
          onClick={handleNext}
          disabled={currentStep === steps.length}
          className={styles.submitButton}
        >
          Next Step
        </button>
      </div>
    </div>
  );
}
