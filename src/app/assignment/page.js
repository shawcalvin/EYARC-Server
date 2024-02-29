import React from "react";
import { StudentProgress } from "./studt_progress";

const exampleAssignment = {
  assignmentID: 16854,
  title: "Demo Assignment",
  type: 'gpt_interview',
  instructorName: 'Bro Wood', 
  dueDate: "04-31-24",
  optional: false,
  duration: 30,
  learningContent: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  solution: "Solution/Feedback",
};

const exampleInteractiveContent = {
  interactiveContent: "Interactive Content",
}
 
const exampleStudent = {
  studentID: 841351,
  studentName: "Trophy Student"
}

export default function Page() {
    const { assignmentID, title, type, instructorName, dueDate, optional, duration, learningContent, solution } = exampleAssignment;
    const { interactiveContent } = exampleInteractiveContent
    const { studentID, studentName } = exampleStudent

    // Create student progress object
    const progress = new StudentProgress(assignmentID, type, studentID)
    progress.open_assignment()
    progress.save_progress()
    progress.student_score = 50

    return (
    <div className="assignment-container">
    <h2>{title}</h2>
    <p><strong>Optional:</strong> {optional ? "Yes" : "No"}</p>
    <p><strong>Due Date:</strong> {dueDate}</p>
    <p><strong>Assigned By:</strong> {instructorName}</p>
    <p><strong>Time to Complete:</strong> {duration.toString()} minutes</p>
    <p><strong>Completion:</strong> {progress.student_score.toString()}%</p>
    <div className="assignment-content">
      <p>{learningContent}</p>
      <p><strong>Interactive Content:</strong> {interactiveContent}</p>
    </div>
    <div className="assignment-solution">
      <h3>Solution/Feedback</h3>
      <p>{solution}</p>
    </div>
    </div>
  );
}