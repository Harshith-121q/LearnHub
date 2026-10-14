package com.learnhub.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;

/**
 * Item sequence specifier for reordering modules or lessons.
 */
public class ReorderItemRequest {

    @NotNull(message = "Item id is required")
    private Long id;

    @NotNull(message = "Sequence order is required")
    @Min(value = 1, message = "Sequence order must be at least 1")
    private Integer sequenceOrder;

    public ReorderItemRequest() {
    }

    public ReorderItemRequest(Long id, Integer sequenceOrder) {
        this.id = id;
        this.sequenceOrder = sequenceOrder;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getSequenceOrder() {
        return sequenceOrder;
    }

    public void setSequenceOrder(Integer sequenceOrder) {
        this.sequenceOrder = sequenceOrder;
    }
}
