"use client"
import { PencilLine } from "lucide-react"
import Icon from "../atoms/Icon"

const TaskItem = ({ task, onEdit, onDelete, onToggleComplete }) => {
  const formattedDate = new Date(task.created_at).toLocaleString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  })

  return (
    <div className="bg-[#D0D0D0] p-3 rounded mb-2 flex justify-between items-center"> 
      <div>
        <div className="flex items-center mb-1">
          <p className="font-normal">{task.title}</p>
          <PencilLine  size={14} className="ml-1 cursor-pointer text-[#33363F] hover:text-red-600" onClick={() => onEdit(task)} />
        </div>
        <p className="text-xs text-[#000000]">{formattedDate}</p>
      </div>
      <div className="flex space-x-1">
        <button
          onClick={() => onToggleComplete(task.id)}
          className="rounded-full w-5 h-5 flex items-center justify-center bg-white hover:bg-gray-400"
        >
          {task.is_done && <Icon name="check" />}
        </button>
        <button
          onClick={() => onDelete(task.id)}
          className="rounded-full w-5 h-5 flex items-center justify-center bg-gray-200 border-1 hover:bg-gray-400"
        >
          <Icon name="delete" />
        </button>
      </div>
    </div>
  )
}

export default TaskItem
