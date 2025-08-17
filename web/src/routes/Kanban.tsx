// src/routes/Kanban.tsx
import { useState } from "react";

const columns = ["New","Waiting","Action Needed","Scheduled","Done"];

export default function Kanban(){
  const [tasks, setTasks] = useState([
    {id:1,title:"New lead: review and reply",status:"New"},
    {id:2,title:"Invoice/payment: follow up",status:"Action Needed"},
  ]);

  return (
    <div className="grid grid-cols-5 gap-3 p-4">
      {columns.map(col => (
        <div key={col} className="bg-gray-50 rounded p-2">
          <h3 className="font-semibold mb-2">{col}</h3>
          {tasks.filter(t=>t.status===col).map(t=>(
            <div key={t.id} className="bg-white border rounded p-2 mb-2">{t.title}</div>
          ))}
        </div>
      ))}
    </div>
  );
}
