import { useEffect, useState } from "react";
import axios from "axios";

function Allstudents() {

  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  async function getStudents() {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/allstudent"
      );

      console.log(response.data);

      setStudents(response.data);

    } catch (error) {

      console.log(error);

      alert("Unable to fetch students");

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    getStudents();

  }, []);


  if (loading) {
    return <h2>Loading students...</h2>;
  }


  return (
    <div className="page-container">

      <h1>All Students</h1>

      <div className="table-container">

        <table>

          <thead>

            <tr>
              <th>Roll Number</th>
              <th>Name</th>
              <th>Age</th>
            </tr>

          </thead>


          <tbody>

            {students.length === 0 ? (

              <tr>
                <td colSpan="3">
                  No students found
                </td>
              </tr>

            ) : (

              students.map((student) => (

                <tr key={student.roll}>

                  <td>{student.roll}</td>

                  <td>{student.name}</td>

                  <td>{student.age}</td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Allstudents;

