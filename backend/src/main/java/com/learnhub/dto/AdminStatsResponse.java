package com.learnhub.dto;

/**
 * Summary metrics for the administrative overview dashboard.
 */
public class AdminStatsResponse {

    private long totalCourses;
    private long publishedCourses;
    private long draftCourses;
    private long archivedCourses;
    private long totalStudents;
    private long totalInstructors;
    private long totalEnrollments;

    public AdminStatsResponse() {
    }

    public AdminStatsResponse(long totalCourses, long publishedCourses, long draftCourses,
                              long archivedCourses, long totalStudents, long totalInstructors,
                              long totalEnrollments) {
        this.totalCourses = totalCourses;
        this.publishedCourses = publishedCourses;
        this.draftCourses = draftCourses;
        this.archivedCourses = archivedCourses;
        this.totalStudents = totalStudents;
        this.totalInstructors = totalInstructors;
        this.totalEnrollments = totalEnrollments;
    }

    public long getTotalCourses() {
        return totalCourses;
    }

    public void setTotalCourses(long totalCourses) {
        this.totalCourses = totalCourses;
    }

    public long getPublishedCourses() {
        return publishedCourses;
    }

    public void setPublishedCourses(long publishedCourses) {
        this.publishedCourses = publishedCourses;
    }

    public long getDraftCourses() {
        return draftCourses;
    }

    public void setDraftCourses(long draftCourses) {
        this.draftCourses = draftCourses;
    }

    public long getArchivedCourses() {
        return archivedCourses;
    }

    public void setArchivedCourses(long archivedCourses) {
        this.archivedCourses = archivedCourses;
    }

    public long getTotalStudents() {
        return totalStudents;
    }

    public void setTotalStudents(long totalStudents) {
        this.totalStudents = totalStudents;
    }

    public long getTotalInstructors() {
        return totalInstructors;
    }

    public void setTotalInstructors(long totalInstructors) {
        this.totalInstructors = totalInstructors;
    }

    public long getTotalEnrollments() {
        return totalEnrollments;
    }

    public void setTotalEnrollments(long totalEnrollments) {
        this.totalEnrollments = totalEnrollments;
    }
}
