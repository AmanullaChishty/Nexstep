// src/routes/BookingLink.tsx
import { useMemo } from "react";

export default function BookingLink(){
  const slots = useMemo(()=>[
    "Tue 10:00","Tue 10:30","Tue 11:00","Tue 11:30","Tue 14:00"
  ],[]);
  return (
    <div className="max-w-md mx-auto p-6">
      <h1 className="text-xl font-semibold mb-4">Book a meeting</h1>
      <div className="grid grid-cols-2 gap-2">
        {slots.map(s=>(
          <button key={s} className="border rounded p-2 hover:bg-gray-50">{s}</button>
        ))}
      </div>
    </div>
  );
}
