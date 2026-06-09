"use client";

import { useEffect, useState } from "react";
import api from "../services/api";

export default function Home() {
  const [leads, setLeads] = useState([]);
  const [filter, setFilter] = useState("All");

  useEffect(() => {
    fetchLeads();
  }, []);

  const fetchLeads = async () => {
    const response = await api.get("/leads");
    setLeads(response.data);
  };

  const filteredLeads =
    filter === "All"
      ? leads
      : leads.filter(
          (lead) => lead.classification === filter
        );

  const markContacted = async (id) => {
    await api.patch(`/lead/${id}`);

    fetchLeads();
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">
        Lead Dashboard
      </h1>

      <select
        className="border p-2 mb-4"
        value={filter}
        onChange={(e) =>
          setFilter(e.target.value)
        }
      >
        <option>All</option>
        <option>Hot</option>
        <option>Warm</option>
        <option>Cold</option>
      </select>

      <table className="w-full border border-gray-300">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Source</th>
            <th>Message</th>
            <th>Classification</th>
            <th>Reply</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {filteredLeads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.name}</td>
              <td>{lead.email}</td>
              <td>{lead.phone}</td>
              <td>{lead.source}</td>

              <td>
                {lead.message.slice(0, 50)}
              </td>

              <td>
                <span
                    className={
                    lead.classification === "Hot"
                        ? "text-red-600 font-bold"
                        : lead.classification === "Warm"
                        ? "text-yellow-600 font-bold"
                        : "text-gray-600 font-bold"
                    }
                >
                    {lead.classification}
                </span>
              </td>

              <td>
                {lead.suggested_reply}
              </td>

              <td>{lead.status}</td>

              <td>
                <button
                    className="bg-blue-500 text-white px-2 py-1 rounded"
                    onClick={() =>
                        markContacted(lead.id)
                    }
                  >
                    Contacted
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}