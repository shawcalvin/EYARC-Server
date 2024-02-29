export class StudentProgress{
  constructor(assignment_id, assignment_type, student_id) {
    this.assignment_id = assignment_id,
    this.assignment_type = assignment_type,
    this.student_id = student_id,
    this.student_interactions = [],
    this.student_score = 0
    this.opened_on
  }

  open_assignment() {
    this.opened_on = Date.now()
  }

  recordInteraction(new_interaction) {
    this.student_interactions.push(new_interaction)
  }

  async recordResults() {
    // calculate percentage score
    this.student_score = 50
    
    // compile results
    const results = {score: this.student_score, interactions: this.student_interactions}
    
    // add results to local storage
    localStorage.setItem('results', results)

    // POST Request to store results in DB
    /*const response = await fetch('/api/assignment/results', {
      method: 'POST',
      headers: {'content-type': 'application/json'},
      body: JSON.stringify(results)
    })*/
  }
}