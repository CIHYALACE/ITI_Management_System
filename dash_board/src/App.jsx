import { useEffect, useState } from "react";

//  course_id |   course_name    | course_duration | course_fee | course_trainer | course_start_date | course_end_date
function App() {
  const [data, setData] = useState({ courses: [], trainees: [] });

  useEffect(() => {
    fetch("http://localhost:8000/api/data")
    .then(response => response.json())
    .then(data => setData(data))
    .catch(error => console.error("Error:", error));
  
  }, []);

  return (
    <div className="container">
      <h1>Data from Django API:</h1>

      <h2>Courses</h2>
      <table className="table table-striped text-center">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">course_id</th>
            <th scope="col">course_name</th>
            <th scope="col">course_duration</th>
            <th scope="col">course_fee</th>
            <th scope="col">course_trainer</th>
            <th scope="col">course_start_date</th>
            <th scope="col">course_end_date</th>
          </tr>
        </thead>
        <tbody>
          {data.courses ? (
            data.courses.map((course, index) => (
              <tr key={index}>
                <th scope="row"></th>
                <td>{course.course_id}</td>
                <td>{course.course_name}</td>
                <td>{course.course_duration}</td>
                <td>{course.course_fee}</td>
                <td>{course.course_trainer}</td>
                <td>{course.course_start_date}</td>
                <td>{course.course_end_date}</td>
                <td> <a className="btn btn-primary" href="#" > Details </a> </td>

              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5" style={{ textAlign: "center" }}>Loading...</td>
            </tr>
          )}
        </tbody>
      </table>

      <h2>Trainees</h2>
      <table className="table table-striped text-center">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">trainee_id</th>
            <th scope="col">trainee_name</th>
            <th scope="col">trainee_email</th>
            <th scope="col">trainee_phone</th>
            <th scope="col">trainee_address</th>
            <th scope="col">trainee_image</th>
          </tr>
        </thead>
        <tbody>
          {data.trainees.length > 0 ? (
            data.trainees.map((trainee, index) => (
              <tr key={index}>
                <th scope="row"></th>
                <td>{trainee.trainee_id}</td>
                <td>{trainee.trainee_first_name} {trainee.trainee_last_name}</td>
                <td>{trainee.trainee_email}</td>
                <td>{trainee.trainee_phone}</td>
                <td>{trainee.trainee_address}</td>
                <td><img src={"https://bootdey.com/img/Content/avatar/avatar7.png"} alt="Trainee" width="50" height="50" /></td>
                <td> <a className="btn btn-primary" href="#" > Profile </a> </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="8" style={{ textAlign: "center" }}>Loading...</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
