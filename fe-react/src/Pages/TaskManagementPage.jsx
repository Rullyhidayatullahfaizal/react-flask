"use client"

import { useState, useEffect } from "react"
import TaskManagementTemplate from "../components/templates/TaskManagementTemplate"

const API_URL = import.meta.env.VITE_API_URL;

const TaskManagementPage = () => {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [task, setTask] = useState({ id: "", title: "", is_done: false })
  const [isEditing, setIsEditing] = useState(false)

  useEffect(() => {
    const fetchTasks = async () => {
        try {
          const res = await fetch(`${API_URL}`)
        if (!res.ok) throw new Error("Failed to fetch tasks")
          const response = await res.json()
        const mergedTasks = [...response.data.undone, ...response.data.done]
        setTasks(mergedTasks)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }
  
    fetchTasks()
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (task.title.trim() === "") return

    try {
      if (isEditing) {
        await fetch(`${API_URL}/${task.id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ title: task.title }),
        })
      } else {
        await fetch(`${API_URL}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ title: task.title }),
        })
      }

      // Refresh data
      const res = await fetch(`${API_URL}`)
      const json = await res.json()
      setTasks([...json.data.undone, ...json.data.done])
      setTask({ id: "", title: "", is_done: false })
      setIsEditing(false)
    } catch (err) {
      console.error("Submit failed:", err)
    }
  }


  const handleEdit = (taskToEdit) => {
    setTask(taskToEdit)
    setIsEditing(true)
  }

  const handleCancel = () => {
    setTask({ id: "", title: "", is_done: false })
    setIsEditing(false)
  }

  const handleDelete = async (id) => {
    try {
      await fetch(`${API_URL}/${id}`, {
        method: "DELETE",
      })
      setTasks(tasks.filter((t) => t.id !== id))
    } catch (err) {
      console.error("Delete failed:", err)
    }
  }

  const handleToggleComplete = async (id) => {
    const taskToUpdate = tasks.find((t) => t.id === id)
    if (!taskToUpdate) return

    try {
      await fetch(`${API_URL}/done/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ is_done: !taskToUpdate.is_done }),
      })

      const res = await fetch(`${API_URL}`)
      const json = await res.json()
      setTasks([...json.data.undone, ...json.data.done])
    } catch (err) {
      console.error("Toggle failed:", err)
    }
  }

  // Filter tasks by is done or undone status
  const ongoingTasks = tasks.filter((task) => !task.is_done)
  const completedTasks = tasks.filter((task) => task.is_done)

  return (
    <TaskManagementTemplate
      task={task}
      setTask={setTask}
      isEditing={isEditing}
      handleSubmit={handleSubmit}
      handleCancel={handleCancel}
      ongoingTasks={ongoingTasks}
      completedTasks={completedTasks}
      onEdit={handleEdit}
      onDelete={handleDelete}
      onToggleComplete={handleToggleComplete}
      loading={loading}
      error={error}
    />
  )
}

export default TaskManagementPage
